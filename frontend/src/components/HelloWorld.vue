<template>
	<div class="columns-1 w-screen">
		<h1 class="p-16 text-center">هر سوالی داری میتونی از من بپرسی</h1>
	</div>
	<div class="container mx-auto content-center">
		<div
			class="rounded-2xl border-gray-700 content-center shadow-2xl mx-auto w-100 md:w-150 lg:w-200"
		>
			<textarea
				name="text"
				id="text"
				placeholder="...سوالت رو بپرس"
				class="h-full w-full mr-3 mt-3 px-4 py-2 text-right"
			></textarea>
			<div class="grid grid-cols-2">
				<div>
					<!-- <button
						type="button"
						class="float-left focus:outline-none text-white bg-green-700 hover:bg-green-800 focus:ring-4 focus:ring-green-300 font-medium rounded-lg text-sm ml-4 px-5 py-2.5 me-2 mb-2 dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800"
					>
						send
					</button> -->
					<div class="w-17 h-10 hover:bg-gray-200 rounded-sm text-center ml-3">
						<div class="grid grid-cols-2">
							<div class="w-5 h-5">
								<img
									src="../assets/attach-file.png"
									class="w-5 h-5 mt-3"
									alt=""
								/>
							</div>
							<div class="mt-2 font-bold">ارسال</div>
						</div>
					</div>
				</div>
				<div>
					<button
						class="bg-blue-600 hover:bg-blue-800 text-white foucs:ring-blue-300 font-bold rounded-lg text-sm px-5 py-2.5 me-2 mb-2 float-right"
					>
						وضعیت
					</button>
				</div>
			</div>
		</div>
		<p class="text-center mt-10 text-gray-400">
			...با پیام دادن به من شما <a href="#">شرایط و قوانین</a> رو قبول میکنین
		</p>
	</div>
</template>
