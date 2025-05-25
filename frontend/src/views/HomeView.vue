<script setup>
import { ref, onMounted } from "vue";
import router from "../router";
import axios from "axios";

import navbar from "../components/navbar.vue";
import aichat from "../components/aichat.vue";
import userchat from "../components/userchat.vue";

// اطلاعات کاربر
const username = ref("");
const email = ref("");
const picture = ref("");
const balance = ref("");

// پیام و اطلاعات چت
const chatresponse = ref([]);
const content = ref("");
const sessionid = ref("");
const url = "http://192.168.10.107:8000/"
// اسکرول به پایین چت
const endOfChat = ref(null);
function scrollToBottom() {
	endOfChat.value?.scrollIntoView({ behavior: "smooth" });
}

// تنظیم هدرهای احراز هویت
const axiosConfig = {
	headers: {
		Authorization: `Bearer ${localStorage.getItem("token")}`,
	},
};

// ارسال پیام در سشن موجود
async function sendmessage() {
	try {
		await axios.post(url + "/chat/", {
			content: content.value,
			sessionid: sessionid.value,
		}, axiosConfig);

		content.value = "";
		await getandsetdata();
		scrollToBottom();
	} catch (error) {
		console.error("Error sending message:", error);
	}
}

// اولین پیام → ساخت سشن جدید + ارسال پیام
async function sendfirstmessage() {
	try {
		const sessionResp = await axios.post(
			url + "/session/create/",
			{ title: content.value },
			axiosConfig
		);
		sessionid.value = String(sessionResp.data.sessionid);
		await sendmessage(); // حالا پیام رو بفرست
	} catch (error) {
		console.error("Error creating session:", error);
	}
}

// گرفتن اطلاعات کاربر و چت‌ها
async function getandsetdata() {
	if (!localStorage.getItem("token")) {
		return router.push("login");
	}
	try {
		const userResp = await axios.get(url + "/whoami/", axiosConfig);
		if (!userResp.data.username) return router.push("login");

		username.value = userResp.data.username;
		email.value = userResp.data.email;
		picture.value = url + "" + userResp.data.image.image;
		balance.value = userResp.data.balance;

		const chatResp = await axios.get(url + "/chats/", axiosConfig);
		if (chatResp.data.length > 0) {
			chatresponse.value = chatResp.data[0].messages;
			sessionid.value = chatResp.data[0].id;
			scrollToBottom();
		}
	} catch (error) {
		router.push("login");
	}
}

onMounted(() => {
	getandsetdata();
});

defineExpose({ getandsetdata, sendmessage, scrollToBottom });
</script>

<template>
	<navbar :username="username" :email="email" :picture="picture" :balance="Number(balance)" />

	<div v-if="chatresponse.length" class="container w-screen">
		<div id="scroll" class="flex flex-col gap-4 mt-30 max-w-6xl px-4 mb-40 mx-auto">
			<template v-for="chat in chatresponse" :key="chat.id">
				<aichat v-if="chat.role === 'assistant'" :data="chat" />
				<userchat v-else :data="chat" />
			</template>
		</div>
		<div ref="endOfChat" class="mb-50"></div>

		<!-- ارسال پیام -->
		<div class="container mx-auto fixed bottom-0">
			<div class="rounded-2xl border-gray-700 bg-white border mb-3 shadow-2xl mx-auto w-100 md:w-150 lg:w-200">
				<textarea v-model="content" placeholder="...سوالت رو بپرس"
					class="h-full w-full mr-3 mt-3 px-4 py-2 text-right"></textarea>
				<div class="text-right px-4 pb-3">
					<button @click="sendmessage" class="px-4 py-1 bg-gray-200 rounded font-bold">ارسال</button>
				</div>
			</div>
		</div>
	</div>

	<!-- وقتی هنوز چتی وجود نداره -->
	<template v-else>
		<div class="columns-1 w-screen">
			<div class="text-center p-16">
				<h1 class="text-4xl md:text-5xl">هر سوالی داری می‌تونی از من بپرسی</h1>
			</div>

			<div class="container mx-auto content-center">
				<div class="rounded-2xl border-gray-700 shadow-2xl mx-auto w-100 md:w-150 lg:w-200">
					<textarea v-model="content" placeholder="...سوالت رو بپرس"
						class="h-full w-full mr-3 mt-3 px-4 py-2 text-right"></textarea>
					<div class="text-right px-4 pb-3">
						<button @click="sendfirstmessage" class="px-4 py-1 bg-gray-200 rounded font-bold">ارسال</button>
					</div>
				</div>
				<p class="text-center mt-10 text-gray-400">
					با پیام دادن به من، شما <a href="#" class="underline">شرایط و قوانین</a> رو قبول می‌کنید.
				</p>
			</div>
		</div>
	</template>
</template>
