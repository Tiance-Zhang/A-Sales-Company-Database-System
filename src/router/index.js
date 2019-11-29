import Vue from 'vue'
import VueRouter from 'vue-router'
import Account from "@/views/Account";
import Transactions from "@/views/Transactions";
import Products from "@/views/Products";
import Stores from "@/views/Stores";
import Login from "@/views/Login";
import Signup from "@/views/Signup";

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Products',
    component: Products
  }, {
    path: '/account',
    name: 'Account',
    component: Account
  }, {
    path: '/transactions',
    name: 'Transactions',
    component: Transactions
  }, {
    path: '/stores',
    name: 'Stores',
    component: Stores
  }, {
    path: '/login',
    name: 'Login',
    component: Login
  }, {
    path: '/signup',
    name: 'Signup',
    component: Signup
  },


];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router
