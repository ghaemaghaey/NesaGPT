<script setup>
const props = defineProps({
data:Object
});
</script>
<template>
	<div class="self-end bg-gray-500 text-white p-4  rounded-2xl shadow-2xl max-w-sm text-right">
		<h2 class="font-black">{{data.role}}</h2>
		<p class="font-light whitespace-pre-line break-words">
{{data.content}}
		</p>
		        <p class="text-gray-700 text-xs">{{ data.jalali_created_at }}</p>
	</div>

</template>