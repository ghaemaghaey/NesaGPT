<script setup>
	import HelloWorld from "../components/HelloWorld.vue";
	import axios from "axios";
	import Chat from "../components/chat.vue";
	import navbar from "../components/navbar.vue";
	import { onMounted, ref } from "vue";
	import router from "../router";
	const username = ref("");
	const email = ref("");
	const picture = ref("");
	const balance = ref("");
	onMounted(() => {
		if (localStorage.getItem("token")) {
			try {
				const resp = axios
					.get("http://127.0.0.1:8000/whoami/", {
						headers: {
							Authorization: `Bearer ${localStorage.getItem("token")}`,
						},
					})
					.then((resp) => {
						if (resp.data.username) {
							console.log(resp.data.username);
							username.value = resp.data.username;
							email.value = resp.data.email;
							picture.value = "http://127.0.0.1:8000" + resp.data.image.image;
							balance.value = resp.data.balance;
						} else {
							router.push("login");
						}
					})
					.catch((err) => {
						router.push("login");
					});
			} catch (err) {
				router.push("login");
			}
		} else {
			router.push("login");
		}
	});
</script>

<template>
	<navbar
		:username="username"
		:email="email"
		:picture="picture"
		:balance="balance"
	/>
	<!-- <Chat /> -->
	<HelloWorld />
</template>
