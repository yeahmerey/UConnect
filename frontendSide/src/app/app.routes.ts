import { Routes } from '@angular/router';
import { AuthComponent } from './features/auth/auth.component';
import { HomeComponent } from './features/home/home.component';
import { PostDetailComponent } from './features/post-detail/post-detail.component';
import { RegisterComponent } from './features/register/register.component';
import { ProfileComponent } from './features/profile/profile.component';

export const routes: Routes = [ 
    {
        path : 'auth' , component : AuthComponent , title : 'Вход'
    }, 
    {
        path : 'register', component : RegisterComponent , title : 'Регистрация'
    },
    {
        path : '' , component : HomeComponent , title : 'UConnect'
    }, 
    {
        path : 'posts/:id' , component :PostDetailComponent , title : 'Post page'
    },
    { 
        path: 'profile/:username', component: ProfileComponent, title : 'Profile page'
    },
];
