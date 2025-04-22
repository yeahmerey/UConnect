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
  comments: any[] = []; 
  loading = true ;
  
  constructor(
    private route: ActivatedRoute,
    private postService : PostsService
  ){}
  
  ngOnInit(): void {
    const id = Number(this.route.snapshot.paramMap.get('id')); 
    this.loadPostAndComments(id); 
  }
  
  loadPostAndComments(postId : number): void{
    this.loading = true ;
    
    this.postService.getPostById(postId).subscribe({
      next: (post) => {
        this.post = post ; 
        this.loadComments(postId); 
      }
    }); 
  }
  loadComments(postId :number) : void{
    this.postService.getPostComments(postId).subscribe({
      next : (comments) => {
        this.comments = comments ;
        this.loading = false ;
      }
    })
  }
}