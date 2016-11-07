/**
 * Created by shimon on 11/4/16.
 */
import {Component} from "@angular/core";
import {UserModel} from "./user";
import {Http, Response, Headers, RequestOptions} from "@angular/http";
import 'rxjs/add/observable/throw';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
//import 'rxjs/add/operator/throw';


@Component({
    selector:'registration-form',
    templateUrl:'/ngapps/registration/registration.html'
})
export class RegistrationForm{
    user:UserModel;
    submitted:boolean;
    vstatus: JSON;

    constructor(private http:Http){
        this.user = new UserModel('', '', '', '', '');
        this.submitted = false;
        this.vstatus ={"success":false, "msg_stack":[]};
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
        let headers = new Headers({"Content-Type":"application/json"});
        let options = new RequestOptions({headers:headers});
        this.http.post('register', JSON.stringify(this.user), options)
                        .map(response => {return response.json();})
                        .subscribe(
                            vstatus => this.vstatus = vstatus,
                            error => console.log(error)
                        );
        this.submitted = true;
        console.log(this.vstatus);
        console.log(this.diagnostic);
        return false;
    }

    get diagnostic(){
        return JSON.stringify(this.user);
    }
}
