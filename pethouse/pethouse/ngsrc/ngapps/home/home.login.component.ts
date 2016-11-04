/**
 * Created by shimon on 11/4/16.
 */
import {Component} from "@angular/core";
import {UserLoginModel} from "./user";


@Component({
    selector:'login-form',
    templateUrl:'/ngapps/home/login.html'
})
export class HomeLoginComponent{
    user:UserLoginModel;

    constructor(){
        this.user = new UserLoginModel('', '');
    }

    get isNameEmpty(){
        if(this.user.username.trim() !== '')
            return false;
        return true;
    }

    get isPasswordEmpty(){
        if(this.user.password.trim() !== '')
            return false;
        return true;
    }

    onSubmit(){
        console.log(JSON.stringify(this.user));
    }
}
