<!-- پیام از ربات -->
<script setup>
const props = defineProps({data:Object});

</script>

<template>
    <div class="self-start bg-gray-700 text-white p-4 rounded-2xl shadow-2xl max-w-sm">
        <h2 class="font-black">NesaGPT</h2>
        <p class="font-light">
{{ data.content }}
        </p>
        <p class="text-gray-500 text-xs">{{ data.jalali_created_at }}</p>
    </div>

</template>
