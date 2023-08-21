<template>
    <div class="home">
      <div class="d-flex flex-wrap justify-content-around mt-4">
        <div>
          <h3 class="text-sm-left">Please Be Patient</h3>
          <h5>Looking for {{ searchForShow }}</h5>
        </div>
        <div>
          <input
            type="text"
            class="form-control"
            placeholder="Search for a show or venue"
            aria-label="Search for a show or venue"
            @keyup.enter="searchShow(searchForShow)"
            v-model="searchForShow"
            aria-describedby="button-addon2"
          >
        </div>
      </div>
      <div class="d-flex flex-wrap">
        <div v-for="(item, index) in searchResults.showDetails" :key="index">
            <div class="bg-custom-card">
              <div class="text-center"><h3>{{ item[1] }}</h3></div>
              <br>
              <div class="text-center"><h5>Timing: {{ item[3] }}</h5></div>
              <br>
              <div class="text-center"><h5>Genre: {{ item[4] }}</h5></div>
              <br>
              <div class="text-center"><h5>Number of Tickets:   {{ item[2] }}</h5></div>
              <br>
              <div class="text-center"><h5>Price: {{ item[5] }}</h5></div>
              <br>
              <div class="text-center"><h5>Rating: {{ item[2] }}</h5></div>
              <br>
              <div class="text-center"><h5>Venue: {{ item[6] }}</h5></div>
            </div>
        
        </div>
      </div>
      <div class="d-flex flex-wrap">
        <div v-for="(venue, index) in searchResults.venueDetails" :key="index">
        
            <div class="bg-custom-card">
              <div class="text-center"><h3>Venue Name: {{ venue[1] }}</h3></div>
              <br>
              <div class="text-center"><h3>Place of the Venue: {{ venue[2] }}</h3></div>
              <br>
              <div class="text-center"><h3>Location of the Venue: {{ venue[3] }}</h3></div>
              <br>
              <div class="text-center"><h3>Capacity for each show: {{ venue[4] }}</h3></div>
              <br>
              <!-- Display venue information here -->
            </div>

        </div>
      </div>
      <div>
        <button class="btn btn-primary" @click="goToHome()">Go back to Home</button>
      </div>
    </div>
  </template>

<script>
import axios from 'axios';

export default {
  name: 'searchShow',
  data: function () {
    return {
      searchForShow: '',
      searchResults: {
        showDetails: [],
        venueDetails: []
      }
    };
  },
  methods: {
    searchShow(searchTerm) {
      console.log(searchTerm);
      axios.post('http://127.0.0.1:5000/api/show-search', { showName: searchTerm })
        .then(response => {
          console.log(response.data);
          this.searchResults = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    goToHome() {
            this.$router.push({ name: 'home' });
            this.$router.go();
        }
    },
    created() {
        console.log(this.showName);
        axios.post('http://127.0.0.1:5000/api/show-search',
            { showName: this.showName })
            .then(response => {
                console.log(response.data);
                this.showDetails = response.data.showDetails;
            })
            .catch(error => {
                console.log(error);
            });
    }
}
</script>

<style scoped>
.bg-custom-card {
  background-color: #e6e6e6;
  border-radius: 10px;
  padding: 10px;
  margin: 10px;
  width: 500px;
  height: 500px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
  padding-top: 1.5em;
}
</style>