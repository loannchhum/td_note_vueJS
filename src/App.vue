<script>
import Questionnaire from './components/Questionnaire.vue'
import axios from 'axios'

const data = {
  questionnaires:[]
}

export default {
  name: 'App',
  data(){
    return data;
  },

  mounted(){
    this.loadDB();
  },

  methods:{
    async loadDB(){

      const response = await axios.get('http://localhost:5000/quiz/api/v1.0/questionnaire');
      this.questionnaires = this.mapper(response.data.questionnaires);
    },
    mapper(questionnaires){
      return questionnaires.map(questionnaire => {
        return {
          id: questionnaire.id,
          name: questionnaire.name
        }
      })
    },
    creerQuestionnaire(){

    },

    async supprimerQuestionnaire(questionnaire){
      const supprime=await axios.delete(`http://localhost:5000/quiz/api/v1.0/questionnaire/${questionnaire.id}`);
      if(supprime.status === 200){
        this.questionnaires = this.questionnaires.filter(q => q.id !== questionnaire.id);
      }

    },

    modifierQuestionnaire(){

    }
  },

  components: { Questionnaire }
}

</script>

<template>
  <body>
    <h1>Application </h1>
    <img class="images" src="/img/10738849-autocollant-d-un-signe-de-quiz-de-dessin-anime-vectoriel.jpg">
       <!-- afficher chacun des questionnaires  -->
    <Questionnaire v-for="questionnaire in questionnaires" :Questionnaire="questionnaire" @remove="supprimerQuestionnaire(questionnaire)" @modifier="modifierQuestionnaire(questionnaire)"></Questionnaire>
  </body>
</template>

<style>
html{
  flex-wrap: wrap;

}
body {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
.images{
  height: 10vh;
}

</style>
