import Vue from 'vue'
import VueRouter from 'vue-router'
import Products from "@/views/Products";
import Stores from "@/views/Stores";
import Transactions from "@/views/Transactions";
import Customers from "@/views/Customers";

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
    path: '/customers',
    name: 'Customers',
    component: Customers
  }
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router
