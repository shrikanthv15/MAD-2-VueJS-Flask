<template>
    <div class="booking-container dark-mode">
      <div class="booking-header d-flex justify-content-between p-3">
        <div>
          <h2>Booking Show: {{ showName }} ({{ venueName }})</h2>
        </div>
        <div>
          <p>Time: {{ showDetails.showTime }}</p>
        </div>
      </div>
      <div class="booking-details">
        <div class="available-seats">
          <h4>Available Seats: {{ showCapacity }}</h4>
        </div>
        <div class="seat-input">
          <div class="d-flex justify-content-center">
            <h4 class="m-2">Enter Number of Seats:</h4>
            <input class="m-2" type="number" min="1" placeholder="Enter Number of Seats" v-model="numberOfSeats">
          </div>
          <div class="d-flex justify-content-center">
            <h4 class="m-1">Price:</h4>
            <h4 class="m-1">{{ showDetails.showPrice }}</h4>
          </div>
          <div class="d-flex justify-content-center">
            <h4 class="m-1">Total Price:</h4>
            <h4 class="m-1">{{ showDetails.showPrice * numberOfSeats }}</h4>
          </div>
        </div>
        <div class="book-button">
          <button class="btn btn-primary" @click="bookTicket()">Book Ticket</button>
        </div>
      </div>
    </div>
  </template>
<script>
import axios from 'axios';

export default {
    name: 'bookTicket',
    data() {
        return {
            numberOfSeats: 1,
            totalPrice: 0,
            showCapacity: 0,
            venues: [],
            showList: [],
            showName: this.$route.params.showname,
            venueName: this.$route.params.venuename,
            username: this.$route.params.username,
            venueDetails: {},
            showDetails: {}

        }
    },
    methods: {
        bookTicket() {
            axios.post('http://127.0.0.1:5000/api/bookticket', {
                username: this.username,
                showName: this.showName,
                venueName: this.venueName,
                numberOfSeats: this.numberOfSeats,
                totalPrice: this.showDetails.showPrice * this.numberOfSeats,
            }).then(response => {
                console.log(response.data);
                this.$router.push({ name: 'home' })
            }).catch(error => {
                console.log(error);
            })
        },
        getVenueDetails(venueName) {
            console.log(venueName);
            for(let i=0;i<this.venues.length;i++){
                if(this.venues[i][1] == venueName){
                    let details = {
                        venueName: this.venues[i][1],
                        venueCapacity: this.venues[i][4],
                    }
                    return details;
                }
            }
            return null;

        },
        getShowDetails(showName){
            console.log(showName);
            for(let i=0;i<this.showList.length;i++){
                if(this.showList[i][1] == showName){
                    let details = {
                        showName: this.showList[i][1],
                        showTime: this.showList[i][3],
                        showPrice: this.showList[i][5],
                        showCapacity: this.showList[i][7],
                    }
                    return details;
                }
            }
            return null;
        }
    },


    created() {
        axios.get('http://127.0.0.1:5000/api/all-details').then(
            response => {
                console.log(response.data);
                this.venues = response.data.VenueList;
                this.showList = response.data.ShowList;
                this.venueDetails = this.getVenueDetails(this.venueName);
                this.showDetails = this.getShowDetails(this.showName);

                this.showCapacity = this.showDetails.showCapacity;
            }
        ).catch(error => {
            console.log(error);
        }
        );

        
        
        
    },
    mounted() {
        this.venueDetails = this.getVenueDetails(this.venueName);
        console.log(this.venueDetails);
        
    }
}



</script>

<style scoped>
.booking-container {
  background-color: #121212;
  color: #ffffff;
  transition: background-color 0.3s, color 0.3s;
  height: 688px;
}

.booking-header {
  border-bottom: 1px solid #555;
}

.booking-details {
  padding: 20px;
  border: 1px solid #555;
  border-radius: 8px;
  margin-top: 20px;
}

.available-seats {
  font-size: 18px;
  margin-bottom: 10px;
}

.seat-input input {
  background-color: #222;
  color: #ffffff;
  border: none;
  padding: 8px;
  border-radius: 4px;
  font-size: 16px;
}

.book-button button {
  background-color: #1976D2;
  color: #ffffff;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  font-size: 18px;
  cursor: pointer;
  transition: background-color 0.3s, color 0.3s;
}

.dark-mode {
  background-color: #121212;
  color: #ffffff;
}

/* Dark mode styles */
.dark-mode .booking-header {
  border-bottom: 1px solid #444;
}

.dark-mode .booking-details {
  border: 1px solid #444;
}

.dark-mode .available-seats {
  color: #cccccc;
}

.dark-mode .seat-input input {
  background-color: #333;
  color: #ffffff;
}

.dark-mode .book-button button {
  background-color: #2196F3;
  color: #ffffff;
}
</style>