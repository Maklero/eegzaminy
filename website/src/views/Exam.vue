<template>
  <div class="exam-container">
    <form class="exam">
      <Question
        v-for="(question, index) in examData.questions"
        :names="examData.name"
        :index="index"
        :question="question"
        :key="question.id"
      />
      <input type="hidden" :value="questionsNumbersList" name="list">
      <input type="hidden" :value="examData.title" name="egzam_name"/>
      <button type="button" id="button">Sprawdź</button>
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
  .exam {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
</style>
