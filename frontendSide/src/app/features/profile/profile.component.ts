import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { PostsService } from '../../core/services/posts.service';
import { ProfileService } from '../../core/services/profile.service';  // Сервис для профиля
import { Profile } from '../../core/models';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-profile',
  imports: [CommonModule],
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {
  username: string | null = localStorage.getItem('username');
  profile!: Profile;
  posts: any[] = [];

  constructor(
    private profileService: ProfileService,
    private postsService: PostsService,
    private route: ActivatedRoute
  ) {}

  ngOnInit(): void {
    this.getProfile();
    this.getUserPosts();
  }

  // Получение профиля пользователя
  getProfile(): void {
    const username = this.username;
    if (username) {
      this.profileService.getProfileByUsername(username).subscribe(profile => {
        this.profile = profile;
      });
    }
  }

  // Получение постов пользователя
  getUserPosts(): void {
    if (this.username) {
      this.postsService.getUserPosts(this.username).subscribe(posts => {
        this.posts = posts;
      });
    }
  }
}
