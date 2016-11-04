/**
 * Created by shimon on 11/4/16.
 */
import {Component} from "@angular/core";
import {UserModel} from "./user";


@Component({
    selector:'registration-form',
    templateUrl:'/ngapps/home/registration.html'
})
export class HomeRegistrationForm{
    user:UserModel;
    submitted:boolean;

    constructor(){
        this.user = new UserModel('', '', '', '', '');
        this.submitted = false;
    }

    get isEmptyName(){
        if(this.user.username.trim() !== '')
            return false;
        return true;
    }

    get isFirstNameEmpty(){
        if(this.user.first_name.trim() !== '')
            return false;
        return true;
    }

    get isLastNameEmpty(){
        if(this.user.last_name.trim() !== '')
            return false;
        return true;
    }

    get isPasswordEmpty(){
        if(this.user.password.trim() !== '')
            return false;
        return true;
    }

    get isPasswordRetypeEmpty(){
        if(this.user.password_retype.trim() !== '')
            if(this.user.password === this.user.password_retype)
                return false;
        return true;
    }

    onSubmit(){
        this.submitted = true;
        console.log(this.diagnostic);
        return false;
    }

    get diagnostic(){
        return JSON.stringify(this.user);
    }
}
