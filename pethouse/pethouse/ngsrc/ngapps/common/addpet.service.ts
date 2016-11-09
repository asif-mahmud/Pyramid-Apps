/**
 * Created by shimon on 11/8/16.
 */
import {Injectable, provide} from "@angular/core";
import {Http, Headers, RequestOptions} from "@angular/http";
import {BehaviorSubject} from "rxjs/BehaviorSubject";
import {Observable} from "rxjs/Observable";
import "rxjs/add/operator/map";
import {Pet, PetObj, VStatus} from "common/interfaces";


@Injectable()
export class AddPetService{
    private addPetUrl:string;
    private _pets:BehaviorSubject<PetObj[]>;
    private _status:BehaviorSubject<VStatus>;
    private data_storage:{
        status:VStatus,
        pets:PetObj[]
    };

    constructor(private http:Http){
        this._pets = <BehaviorSubject<PetObj[]>> new BehaviorSubject([]);
        this._status = <BehaviorSubject<VStatus>> new BehaviorSubject({});
        this.data_storage = {
            status:{
                success:false,
                msg_stack:[]
            },
            pets:[]
        };
        this.addPetUrl = '/user/add/pet';
    }

    get pets():Observable<PetObj[]>{
        return this._pets.asObservable();
    }

    get status():Observable<VStatus>{
        return this._status.asObservable();
    }

    load_users_pets(userId:number){
        this.http.get(`/user/${userId}/pets`)
            .map(response => response.json())
            .subscribe(
                (data) => {
                    this.data_storage.pets = data.pets;
                    this._pets.next(Object.assign({},this.data_storage).pets);
                },
                error => console.log(error.message)
            );
    }

    add_pet(pet:Pet){
        let header = new Headers({'Content-Type':'application/json'});
        let options = new RequestOptions({headers:header});
        this.http.post(this.addPetUrl, JSON.stringify(pet), options)
            .map(response => response.json())
            .subscribe(
                (data) => {
                    this.data_storage.status = data.status;
                    /*
                    Insert new pet data only if success
                     */
                    if(this.data_storage.status.success){
                        this.data_storage.pets.push(data.pet);
                        this._pets.next(Object.assign({},this.data_storage).pets);
                        this._status.next(Object.assign({},this.data_storage).status);
                    }
                },
                error => console.log(error.message)
            );
    }
}
