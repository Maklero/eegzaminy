import Vue from 'vue';
import Router from 'vue-router';

import Home from './views/Home.vue';
import Exam from './views/Exam.vue';


Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      comment: Home,
    },
    {
      path: '/about',
      name: 'about',
      component: Home,
    },
    {
      path: '/exam/:name',
      name: 'exam',
      component: Exam,
    },
  ],
});
