<template>
  <div class="question-container">
    <div class="question">
      <h3>Pytanie {{ index + 1 }}</h3>
      <span>{{ question.question }}</span>
    </div>
    <div v-if="question.img">
      <img :src="question.img" :alt="question.img">
    </div>
    <div v-for="(label, index) in names" class="answer">
      <div class="answer-name">
        <input
          type="radio"
          :name="question.id"
          :value="label"
          :id="`o${index}_${question.id}`"
        >
      </div>
      <div class="answer-content">
        <label :for="`o${index}_${question.id}`">
          {{ label }}. {{ question[label] }}
        </label>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Question',
  props: {
    question: {
      type: Object,
      required: true,
    },
    index: {
      type: Number,
      required: true,
    },
    names: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style lang="scss" scoped>
  .question-container {
    margin: 2px 0;
    width: 98%;
    min-height: 100px;
    background-color: red;
    overflow: hidden;

    img {
      width: 100%;
    }
  }
</style>
