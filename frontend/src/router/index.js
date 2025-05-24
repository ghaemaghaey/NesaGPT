import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import ProfileView from "../views/ProfileView.vue";
// import ChatView from "@/views/ChatView.vue";
import LoginView from "../views/login.vue";
// import NotFound from "@/views/NotFound.vue";

const routes = [
	{ path: "/", name: "Home", component: HomeView },
	// { path: "/chat", name: "Chat", component: ChatView },
	{ path: "/login", name: "Login", component: LoginView },
	{ path: "/profile", name: "profile", component: ProfileView },
];

const router = createRouter({
	history: createWebHistory(),
	routes,
});

export default router;
