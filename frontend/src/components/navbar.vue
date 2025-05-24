<script setup>
	import router from "../router";
	const props = defineProps({
		username: String,
		email: String,
		picture: String,
		balance: Int8Array,
	});

	function logout() {
		localStorage.removeItem("token");
		router.push("login");
	}
</script>

<template>
	<div class="container">
		<div
			class="grid grid-cols-3 fixed top-0 right-0 left-0 text-black mt-4 rounded-2xl items-center justify-evenly"
		>
			<div class="text-left flex items-center m-5 font-bold font-mono text-2xl">
				NesaGPT
			</div>
			<div class="font-black text-center mx-auto rounded-2xl hover:bg-gray-400">
				<p class="mt-1">
					مانده کیف پول :
					<span class="text-violet-800">
						{{ balance }}
					</span>
					تومان
				</p>
			</div>
			<div class="">
				<img
					class="rounded-full h-12 w-12 object-cover float-right mr-5"
					:src="picture"
					alt=""
				/>
				<div class="text-right">
					<button
						@click="logout"
						class="hover:bg-gray-300 bg-gray-200 rounded-2xl p-2 mr-3"
					>
						خروج از حساب کاربری
					</button>
				</div>
			</div>
		</div>
	</div>
</template>
