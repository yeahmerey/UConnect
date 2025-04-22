import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { AuthModel, Post, Token } from '../models';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PostsService {

  constructor(private client : HttpClient) { 

  }

  login(authModel : AuthModel): Observable<Token>{
    return this.client.post<Token>('http://127.0.0.1:8000/api/auth/login/' , authModel)
  }

  getPosts(): Observable<Post[]>{
    const access = localStorage.getItem('access')
    
    return this.client.get<Post[]>('http://127.0.0.1:8000/api/posts')
    // return this.client.get<Post[]>('http://127.0.0.1:8000/api/posts/' , 
    //   {headers: {"Authorization":`Bearer ${access}`}})
  }
  getPostById(id: number): Observable<Post> {
    return this.client.get<Post>(`http://127.0.0.1:8000/api/posts/${id}`)
  }
  getPostComments(id: number): Observable<any[]> {
    return this.client.get<any[]>(`http://127.0.0.1:8000/api/posts/${id}/comments`)
  }
}
