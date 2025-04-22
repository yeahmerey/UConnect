import { Component } from '@angular/core';
import { Post } from '../../core/models';
import { POSTS } from '../../core/fake-db';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-home',
  imports: [CommonModule , RouterModule],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {
  posts!: Post[];  

  constructor(){
    this.posts = POSTS;  
  }
}
