import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Post } from '../../core/models';
import { PostsService } from '../../core/services/posts.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-post-detail',
  imports: [CommonModule],
  templateUrl: './post-detail.component.html',
  styleUrl: './post-detail.component.css'
})
export class PostDetailComponent implements OnInit{
  post !: Post; 
  
  constructor(private route: ActivatedRoute , private postService : PostsService){
  }
  
  ngOnInit(): void {
    const id = Number(this.route.snapshot.paramMap.get('id')); 
    this.postService.getPostById(id).subscribe(data => {
      this.post = data ;
    })
  }
}
