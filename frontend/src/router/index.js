import {createRouter, createWebHistory} from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ResultsView from '../views/ResultsView.vue'
import ResultView from '../views/ResultView.vue'
import SettingsView from '../views/SettingsView.vue'
import AuthView from '../views/AuthView.vue'

const routes = [
    {
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/results',
        name: 'results',
        component: ResultsView
    },
    {
        path: '/result/:id',
        name: 'result',
        component: ResultView
    },
    {
        path: '/settings',
        name: 'settings',
        component: SettingsView
    },
    {
        path: '/auth',
        name: 'auth',
        component: AuthView
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
