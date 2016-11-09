/**
 * Created by shimon on 11/9/16.
 */
import {Injectable} from "@angular/core";
import {PetType} from "common/interfaces";
import {BehaviorSubject} from "rxjs/BehaviorSubject";
import {Observable} from "rxjs/Observable";
import {Http} from "@angular/http";
import "rxjs/add/operator/map";


@Injectable()
export class PetTypeService{
    private _pet_types:BehaviorSubject<PetType[]>;
    private data_storage:{
        pet_types:PetType[]
    };
    private base_url:string;

    constructor(private http:Http){
        this._pet_types = <BehaviorSubject<PetType[]>>new BehaviorSubject([]);
        this.data_storage = {pet_types:[]};
        this.base_url = '/services/available/pet/types';
    }

    get pet_types():Observable<PetType[]>{
        return this._pet_types.asObservable();
    }

    load_all(){
        this.http.get(this.base_url)
            .map(response => response.json())
            .subscribe(
                (data) => {
                    this.data_storage.pet_types = data;
                    this._pet_types.next(Object.assign({}, this.data_storage).pet_types);
                },
                error => console.log("Error while loading PetTypes:", error.message)
            )
    }
}
