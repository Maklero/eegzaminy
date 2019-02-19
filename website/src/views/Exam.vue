<template>
  <div class="exam-container">
    <h1 class="title">{{ examData.title }}</h1>
    <form class="exam" id="exam-form">
      <Question
        v-for="(question, index) in examData.questions"
        :names="examData.name"
        :index="index"
        :question="question"
        :key="question.id"
      />
      <input type="hidden" :value="questionsNumbersList" name="list">
      <input type="hidden" :value="examData.title" name="egzam_name"/>
      <button
        type="button"
        class="button"
        id="check-exam"
        @click="checkExam"
      >
        Sprawdź
      </button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
import dataFile from '@/api.json';
import Question from '@/components/Question.vue';

const API = dataFile.url;

export default {
  name: 'Exam',
  components: { Question },
  data() {
    return {
      examName: null,
      examData: null,
      questionsNumbersList: null,
    };
  },
  methods: {
    getExam() {
      axios.get(`${API}/exams/${this.examName}`)
        .then((response) => {
          this.examData = response.data;
          this.questionsNumbersList = '';
          response.data.questions.forEach((row) => {
            this.questionsNumbersList += `${row.id};`;
          });
        })
        .catch(error => console.log(error));
    },
    checkExam() {
      const fm = document.querySelector('#exam-form');
      axios.post(`${API}/verify`, fm)
        .then((response) => {
          console.log(response);
        })
        .catch(error => console.log(error));
    },
  },
  mounted() {
    this.examName = this.$route.params.name;
    this.getExam();
  },
  watch: {
    $route() {
      this.examName = this.$route.params.name;
      this.getExam();
    },
  },
};
</script>

<style lang="scss" scoped>
  .title {
    position: fixed;
    margin: 0;
    top: 0; left: 0;
    width: 100%;
    height: 60px;
    display: flex;
    justify-content: center; align-items: center;
    text-transform: uppercase;
    background-color: #455A64;
    box-shadow: 0 2px 2px black;
    z-index: 19;
  }

  .exam {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .button {
    width: 98%;
  }
</style>
