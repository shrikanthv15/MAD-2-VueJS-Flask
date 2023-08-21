<template>
    <div class="container">
        <h1>Edit Venue</h1>
        <div class="container">
            <div class="">
                Edit Venue: {{ venuename }}
            </div>
            <div class="form-group">
                <input type="text" class="form-control" id="venueName" v-model="name" placeholder="Enter VenueName">
            </div>
            <div>
                <input type="text" class="form-control" id="venuePlace" v-model="place" placeholder="Enter Place">
            </div>
            <div>
                <input type="text" class="form-control" id="venueLocation" v-model="location" placeholder="Enter Location">
            </div>
            <div>
                <input type="text" class="form-control" id="VenueCapacity" v-model="capacity" placeholder="Enter Capacity">
            </div>

            <button class="btn btn-primary mt-3" @click="editVenue()">Save</button>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    data() {
        return {
            name: '',
            place: '',
            location: '',
            capacity: '',
            venueName: this.$route.params.venueName,
            
        };
    },
    methods: {
        editVenue() {
            axios.post('http://127.0.0.1:5000/api/editVenue', {
                venueName: this.name,
                place: this.place,
                location: this.location,
                capacity: this.capacity,
            }).then(response => {
                console.log(response.data);
                this.$router.push({ name: 'adminDashboard' });
            }).catch(error => {
                console.log(error);
            });
        },
    },
    created() {
        axios.post('http://127.0.0.1:5000/api/venueDetails', {
            venueName: this.venueName,
        }).then(response => {
            console.log(response.data.venueDetails[0]);
            this.name = response.data.venueDetails[0][1];
            this.place = response.data.venueDetails[0][2];
            this.location = response.data.venueDetails[0][3];
            this.capacity = response.data.venueDetails[0][4];
            
        }).catch(error => {
            console.log(error);
        })
    }
}
</script>
