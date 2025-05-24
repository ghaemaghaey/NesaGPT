<script setup>
import router from "../router";
const props = defineProps({
	username: String,
	email: String,
	picture: String,
	balance: Number,
});

function logout() {
	localStorage.removeItem("token");
	router.push("login");
}
</script>

<template>
	<div class="container ">
		<div
			class="grid grid-cols-3 bg-white fixed top-0 right-0 left-0 text-black shadow-2xl rounded-2xl items-center justify-evenly">
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
				<img class="rounded-full h-12 w-12 object-cover float-right mr-5" :src="picture" alt="" />
				<div class="text-right ">
					<button @click="logout" class="hover:bg-gray-200 h-10 w-10 p-1 mt-1 mr-4 rounded-2xl ">
						<!-- <img src="../assets/logout.svg" class="w-13 h-13 pt-2" alt=""> -->
						<svg viewBox="-2.4 -2.4 28.80 28.80" fill="none" xmlns="http://www.w3.org/2000/svg"
							transform="matrix(1, 0, 0, 1, 0, 0)rotate(0)" stroke="#000000">
							<g id="SVGRepo_bgCarrier" stroke-width="0"></g>
							<g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"
								stroke="#e60000" stroke-width="0.4800000000000001"></g>
							<g id="SVGRepo_iconCarrier">
								<path
									d="M16 17L21 12M21 12L16 7M21 12H9M9 3H7.8C6.11984 3 5.27976 3 4.63803 3.32698C4.07354 3.6146 3.6146 4.07354 3.32698 4.63803C3 5.27976 3 6.11984 3 7.8V16.2C3 17.8802 3 18.7202 3.32698 19.362C3.6146 19.9265 4.07354 20.3854 4.63803 20.673C5.27976 21 6.11984 21 7.8 21H9"
									stroke="#adfaadf" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">
								</path>
							</g>
						</svg>
					</button>
				</div>
			</div>
		</div>
	</div>
</template>
