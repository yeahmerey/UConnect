import { Component } from '@angular/core';
import { Post } from '../../core/models';
import { POSTS } from '../../core/fake-db';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { Block } from '@angular/compiler';
import { PostsService } from '../../core/services/posts.service';

@Component({
  selector: 'app-home',
  imports: [CommonModule , RouterModule],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {
  posts!: Post[];  
  loaded:boolean = false; 
  
  constructor(private postService:PostsService){

  }
  ngOnInit() : void{
    this.getPosts()
  }
  getPosts(){
    this.postService.getPosts().subscribe((posts) => {
      this.posts = posts; 
      this.loaded = true ;
    })
  }
}
