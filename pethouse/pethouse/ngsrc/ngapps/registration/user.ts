/**
 * Created by shimon on 11/4/16.
 */
export class UserModel{
    constructor(
      public username:string,
      public first_name:string,
      public last_name:string,
      public password:string,
      public password_retype:string
    ){}
}
