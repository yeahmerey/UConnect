export interface User {
    id: number;
    username: string;
    email: string;
  }
  
  export interface Profile {
    id: number;
    user: User;
    bio: string;
    avatar: string | null;
  }
  
  export interface Post {
    id: number;
    user: User;
    content: string;
    created_at: string;
  }
  
  export interface Comment {
    id: number;
    user: User;
    post: number;
    content: string;
    created_at: string;
  }

  export interface AuthModel {
    username : string ; 
    password : string ; 

  }
  export interface Token {
    refresh : string ; 
    access : string ; 
  }