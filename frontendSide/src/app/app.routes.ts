import { Routes } from '@angular/router';
import { AuthComponent } from './features/auth/auth.component';
import { HomeComponent } from './features/home/home.component';
import { PostDetailComponent } from './features/post-detail/post-detail.component';

export const routes: Routes = [ 
    {
        path : 'auth' , component : AuthComponent , title : 'Регистрация'
    }, 
    {
        path : '' , component : HomeComponent , title : 'UConnect'
    }, 
    {
        path : 'posts/:id' , component :PostDetailComponent , title : 'Post page'
    }
];
