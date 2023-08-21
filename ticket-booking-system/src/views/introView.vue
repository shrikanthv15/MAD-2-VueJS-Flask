<template>
  <div class="home bg-custom">
    <!-- <Navbar /> -->
    <div class="container">
      <div class="vertical-center">
      <h1 class="display-3">
        Welcome To GoodSoup Ticket Booking System!
      </h1>
    </div>
    </div>

  </div>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@800&display=swap');

.container {
  height: 200px;
  position: relative;
  border: 3px
}
/* Define the custom background class */
.bg-custom {
  background-image: url('C:/idk/Ticket-Booking-System/ticket-booking-system/src/assets/image.jpg');

  background-size: cover; 
  background-position: center; 
  background-repeat: no-repeat;

  width: 100%; 
  height: 700px; 
}


.vertical-center {
  margin: 0;
  margin-top: 30vh;
  position: absolute;
  top: 50%;
  -ms-transform: translateY(-50%);
  transform: translateY(-50%);
}

.display-3 {
  font-family: 'Poppins', sans-serif;
  font-size: 5rem;
  font-weight: 600 !important;
  line-height: 1.2;
  color: whitesmoke;
  margin-bottom: 1rem;
  margin-top: 1rem;
  text-align: center;
  letter-spacing: -3px;
}
</style>
<script>
import Navbar from '../components/Navbar.vue'


export default {
  name: 'introView',
  components: {
    Navbar,
  },
}
</script>
  