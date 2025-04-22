import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Post } from '../../core/models';
import { POSTS } from '../../core/fake-db';

@Component({
  selector: 'app-post-detail',
  imports: [],
  templateUrl: './post-detail.component.html',
  styleUrl: './post-detail.component.css'
})
export class PostDetailComponent implements OnInit{
  post !: Post; 
  constructor(private route: ActivatedRoute){
  }
  ngOnInit(): void {
    this.route.paramMap.subscribe((params) => {
      const postID = Number(params.get('id')); 
      this.post = POSTS.find(post => post.id ===postID) as Post;
    }); 
  }
}
