<template>
  <div id="app">
    <div class="menu-clicker">
      <HamburgerButton @hamburger="hamburger" />
    </div>
    <div class="nav">
      <router-link to="/">Home</router-link>
      <router-link to="/about">About</router-link>
      <router-link
        v-for="exam in examList"
        :to="`/${exam.route}`"
        :key="exam.route">
        {{ exam.content }}
      </router-link>
    </div>
    <router-view class="content"/>
  </div>
</template>

<script>
import axios from 'axios';
import HamburgerButton from '@/components/HamburgerButton.vue';
import dataFile from '@/api.json';

const API = dataFile.url;

export default {
  components: { HamburgerButton },
  data() {
    return {
      examList: [],
    };
  },
  mounted() {
    axios.get(`${API}/exams/list`)
      .then((response) => {
        const res = response.data.list;
        res.forEach((r) => {
          this.examList.push({
            route: `exam/${r}`,
            content: r.toUpperCase(),
          });
        });
      })
      .catch((error) => {
        console.log(error);
      });
  },
  methods: {
    hamburger: () => {
      const menu = document.querySelector('.hamburger');
      const nav = document.querySelector('.nav');

      menu.classList.toggle('hamburger-active');
      nav.classList.toggle('nav-open');
    },
  },
  watch: {
    $route() {
      const menu = document.querySelector('.hamburger');
      const nav = document.querySelector('.nav');
      // Niestety muszę się powtórzyć, anlaaaki
      menu.classList.remove('hamburger-active');
      nav.classList.remove('nav-open');
    },
  },
};
</script>

<style lang="scss">
  body {
    margin: 0;
    padding: 0;
    background-color: #333;
  }

  * {
    box-sizing: border-box;
  }

  .menu-clicker {
    display: flex;
    align-items: center;
    justify-content: center;
    position: fixed;
    background-color: rgba(69,90,100, .6);
    top: 5px; left: 5px;
    width: 50px; height: 50px;
    border-radius: 50%;
    z-index: 21;
  }

  .nav {
    display: flex;
    flex-direction: column;
    align-items: center;
    position: fixed;
    top: 0;
    width: 100%; height: 100vh;
    padding-top: 60px;
    left: -100%;
    font-size: 2.5em;
    background-color: #455A64;
    opacity: 1;
    z-index: 20;
    transition: left .3s;
  }

  .nav-open {left: 0;}

  a {
    color: white;
    text-decoration: none;
  }

  .content {
    margin-top: 60px;
    padding: 5px;
  }
</style>
