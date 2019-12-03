import Vue from 'vue'
import VueRouter from 'vue-router'
import Products from "@/views/Products";
import Stores from "@/views/Stores";
import Transactions from "@/views/Transactions";
import Users from "@/views/Users";
import Statistics from "@/views/Statistics";
import Login from "@/views/Login"

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Products',
    component: Products
  }, {
    path: '/stores',
    name: 'Stores',
    component: Stores
  },{
    path: '/transactions',
    name: 'Transactions',
    component: Transactions
  }, {
    path: '/users',
    name: 'Users',
    component: Users
  }, {
    path: '/statistics',
    name: 'Statistics',
    component: Statistics
  }, {
    path: '/login',
    name: 'Login',
    component: Login
  }
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router
