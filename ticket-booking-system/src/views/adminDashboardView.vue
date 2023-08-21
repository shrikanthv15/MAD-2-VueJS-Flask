<template>
    <div>
        <button class="btn btn-primary text-center my-auto" v-if="venueListIsEmpty()" @click="createVenue()">Create Venue</button>

        <div class="container">
            <h1>Admin Dashbaord</h1>
            <div class="container border border-bottom-5 venue-container" v-for="venue in venues" :key="venue[1]">
                <div class="d-flex justify-content-between align-items-center">
                    <h1>{{ venue[1] }}</h1>
                    <button type="button" class="btn btn-danger" @click="deleteVenue(venue[1])">Delete Venue</button>
                </div>
                <div class="col-lg-12 px-5 mx-auto mb-4">
                    <button type="button" class="btn btn-primary mt-3 mx-2" @click="editVenue(venue[1])">Edit Venue</button>
                </div>
                <div class="col-lg-12 px-5 mx-auto mb-4">
                    <button class="btn btn-primary" @click="createShow(venue[1], venue[4])">Add Shows</button>
                </div>
                <div class="row col-lg-12 px-5 mx-auto mb-4">
                    <div class="col-lg-4" v-for="show in venueAndShows[venue[1]]" :key="show[1]">
                        <div class="card mb-3">
                            <div class="card-body">
                                <h5 class="card-title">{{ show[1] }}</h5>
                                <h6 class="card-subtitle mb-2 text-body-secondary">time: {{ show[3] }}</h6>
                                <h6 class="card-subtitle mb-2 text-body-secondary">Rating: {{ show[2] }}</h6>
                                <h6 class="card-subtitle mb-2 text-body-secondary">Tag(s): {{ show[4] }}</h6>
                                <h6 class="card-subtitle mb-2 text-body-secondary">Price: {{ show[5] }}</h6>
                                <button type="button" class="btn btn-primary mt-3" @click="editShow(show[1])">Edit Show</button>
                            <br>
                                <button type="button" class="btn btn-primary mt-3" @click="deleteShow(show[1],show[3])">Delete Show</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <button class="btn btn-primary text-center my-auto mt-5 mx-4" v-if="!venueListIsEmpty()" @click="createVenue()">Create Venue</button>
            <button class="btn btn-primary text-center my-auto mt-5" @click="exportVenuePDF()">Export Venue Details</button>
            <button class="btn btn-primary text-center my-auto mx-3 mt-5" @click="exportShowDetails()">Export Show Details</button>
        </div>
    </div>
    
</template>

<style>
.card {
    width: 100%;
}
.venue-container {
    border-radius: 10px;
    padding: 10px;
    margin: 10px;
    background-color: #f2f2f2;
    height: fit-content;
}
</style>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            //Data variables
            venues: [],
            shows: [],
            venueAndShows: {}
        }
    },
    methods: {
        //Methods
        editShow(showname) {
            this.$router.push({ name: 'editShow', params: { showname: showname } })
        },
        deleteVenue(venueName) {
        
            const confirmed = confirm("Are you sure you want to delete this show?");
            if (confirmed) {
            axios.post('http://127.0.0.1:5000/api/deleteVenue', {
                venueName : venueName,
            }).then(response => {
                console.log(response.data);
                this.$router.go(); // Refresh the page after successful deletion
            }).catch(error => {
                console.log(error);
            
            });
        }
        },
        deleteShow(showname, showtime) {
    const confirmed = confirm("Are you sure you want to delete this show?");
    
    if (confirmed) {
        axios.post('http://127.0.0.1:5000/api/deleteShow', {
            showname: showname,
            time: showtime
        }).then(response => {
            console.log(response.data);
            this.$router.go();
        }).catch(error => {
            console.log(error);
        });
    }
},
editVenue(venueName) {
        this.$router.push({ name: 'editVenue', params: { venueName: venueName } });
    },
createVenue() {
            this.$router.push({ name: 'createVenue' })
        },
        venueListIsEmpty() {
            return this.venues.length == 0;
        },
        createShow(venueName, venuecapacity) {
            this.$router.push({
                name: 'createShow', params: {
                    venuename: venueName,
                    venuecapacity: venuecapacity
                }
            })
        },
        async exportVenuePDF() {
    const data = [
        (this.venues, this.shows, this.venueAndShows)
    ];

    try {
        const response = await axios.post('http://127.0.0.1:5000/api/exportVenuePDF', data);
        const pdf_file = response.data.pdf_file;

        // Check if the browser supports the "FileSaver" API for saving files
        if (window.navigator.msSaveOrOpenBlob) {
            // For IE/Edge (use the "downloadPDF" endpoint to download the file)
            window.location.href = `http://127.0.0.1:5000/api/downloadVenuePDF/${pdf_file}`;
        } else {
            // For other browsers (use a link to download the file)
            const downloadLink = document.createElement('a');
            downloadLink.href = `http://127.0.0.1:5000/api/downloadVenuePDF/${pdf_file}`;
            downloadLink.target = '_blank';
            downloadLink.download = 'venue_details.pdf';
            downloadLink.click();
        }

        alert('PDF Generated');
    } catch (error) {
        console.error(error);
        alert('Failed to generate PDF. Please try again.');
    }
},
async exportShowDetails(){
    const data = [(this.show)]

    try {
        const response = await axios.post('http://127.0.0.1:5000/api/exportShowPDF', data);
        const pdf_file = response.data.pdf_file;

        if(window.navigator.msSaveOrOpenBlob){
            window.location.href = `http://127.0.0.1:5000/api/downloadShowPDF/${pdf_file}`;
        }else{
            const downloadLink = document.createElement('a');
            downloadLink.href = `http://127.0.0.1:5000/api/downloadShowPDF/${pdf_file}`;
            downloadLink.target = '_blank';
            downloadLink.download = 'show_details.pdf';
            downloadLink.click();
        }
        alert('PDF Generated');
    } catch (error) {
        console.error(error);
        alert('Failed to generate PDF. Please try again.');
    }

}


    },
    created() {
        //On page load check if there are venues in the database
        axios.get('http://127.0.0.1:5000/api/all-details')
            .then(response => {
                console.log(response.data);
                this.venues = response.data.VenueList;
                this.shows = response.data.ShowList;
                this.venueAndShows = response.data.ShowVenueList;

            })
            .catch(error => {
                console.log(error);
            });
    }
}
</script>