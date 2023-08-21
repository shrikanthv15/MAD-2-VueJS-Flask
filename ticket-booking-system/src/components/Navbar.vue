<template>
  <div id="app">
    <nav class="navbar navbar-expand-md bg-dark">
      <div class="navbar-collapse collapse w-100 order-1 mt-1 order-md-0 dual-collapse2">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item mt-1">
      <router-link class="navbar-brand" to="/"><spam style="color: gold;">Goodsoup</spam></router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/"><spam style="color: gold;">Home</spam></router-link>
          </li>
          <li>
            <router-link class="nav-link" to="/about"><spam style="color: gold;">About</spam></router-link>
          </li>
          <li>
            <router-link class="nav-link" to="/login"><spam style="color: gold;">User Login</spam></router-link>
          </li>
          <li>
            <router-link class="nav-link" to="/admin-login"><spam style="color: gold;">Admin Login</spam></router-link>
          </li>
        </ul>
      </div>
        
          
          <div class="ml-auto">
            <uL>
              <li class="nav-item mt-1 list-unstyled ">
            <button class="button btn-primary btn" v-if="checkLogin()" @click=logout()>Logout</button>
              </li>
            </uL>

          </div>

       
        
    </nav>
    <router-view />
  </div>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap');
/* 
.nav-link {
  color: rgba(50, 6, 90, 1);
  font-family: 'Poppins', sans-serif;
} */
</style>

<script>

export default {
  name: 'Navbar',
  methods: {
    logout() {
      localStorage.removeItem('token');
      if (localStorage.getItem('token') === null) {
        this.$router.push('/intro');
      }
    },
    checkLogin() {
      return localStorage.getItem('token') !== null;

    }
  }
}


</script>