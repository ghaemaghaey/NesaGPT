<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
const router = useRouter()
let accesstoken = ref('')
const username = ref('')
const password = ref('')
const error = ref('')
const animation = ref('')
animation.value = true
const url = "http://192.168.10.107:8000/"
import axios from 'axios';
async function  login (){
    animation.value = false
    error.value = false
    const data = {
        "username": username.value,
        "password": password.value,
    }
    const resp = await axios.post(url+'/api/token/',data).catch(()=>{
        error.value = true
        animation.value = true
    })
    localStorage.setItem('token',resp.data.access)
    router.push({name:'Home'})
    animation.value = true
}


</script>

<template>
	<div class="columns-1 w-screen"></div>
	<div class="container mx-auto content-center">
        <div class="rounded h-50 w-50 mx-auto object-cover mb-20">
            <img src="https://app.nesagholikhani.com/assets/images/nesa-gh.png" alt="">
        </div>
		<div
			class="rounded-2xl content-center border h-15 border-gray-500 mx-auto w-80 md:w-100"
		>
			<input v-model="username"
				name="text"
				id="username"
				placeholder="نام کاربری یا ایمیل خود را وارد کنید "
				class="h-full w-full mr-5 pr-4 text-right"
			></input>
		</div>
		<div
			class="rounded-2xl content-center border mt-3  h-15 border-gray-500 mx-auto w-80 md:w-100"
		>
			<input v-model="password"
            type="password"
				name="password"
				id="password"
				placeholder="رمز عبور خود را وارد کنید "
				class="h-full w-full mr-5 pr-4 text-right"
			></input>
		</div>
        
        
        <div v-if="error" class="text-center">
            <p class="text-red-600 font-black"> نام کاربری یا رمز عبور اشتباه است </p>
        </div>
        <div class="text-center  font-light">
            <button @click="login" class="hover:bg-gray-400 rounded-2xl p-2 text-3xl mt-5" > ورود به حساب کاربری  </button>
            <div>
                <iframe :class="{'invisible': animation}" class="w-65 h-65 mx-auto p-5" src="https://lottie.host/embed/84a91475-fbd9-41b5-9f2c-e20ce09d5220/EJzDcsocVR.lottie"></iframe>
            
            </div>
        </div>
		<p class="text-center mt-10 text-gray-400">
			...با ساختن حساب  شما <a href="#">شرایط و قوانین</a> رو قبول میکنین
		</p>
        <br>

</div>
</template>

