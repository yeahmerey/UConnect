import { Component } from '@angular/core';
import { AuthModel } from '../../core/models';
import { PostsService } from '../../core/services/posts.service';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-auth',
  imports: [FormsModule],
  templateUrl: './auth.component.html',
  styleUrl: './auth.component.css'
})
export class AuthComponent {
  authModel : AuthModel ; 
  constructor(private postService : PostsService){
    this.authModel = {} as AuthModel
  }

  login(){
    this.postService.login(this.authModel).subscribe((token) =>{
      localStorage.setItem('access', token.access); 
      localStorage.setItem('refresh', token.refresh);   
    })
  }
}
