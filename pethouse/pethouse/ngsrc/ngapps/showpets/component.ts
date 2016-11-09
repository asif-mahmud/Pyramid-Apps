/**
 * Created by shimon on 11/8/16.
 */
import {Component, OnInit, ElementRef} from "@angular/core";
import {AddPetService} from "../common/addpet.service";
import {PetObj} from "../common/interfaces";


@Component({
    selector:'pet-collection',
    templateUrl:'/ngapps/showpets/pet.collection.html',
})
export class PetCollectionComponent implements OnInit{
    pets:PetObj[];
    userid:number;

    constructor(
        private addPetService:AddPetService,
        private elementRef:ElementRef
    ){
        this.pets = [];
        this.userid = <number>this.elementRef.nativeElement.getAttribute("userid");
        console.log(this.addPetService);
    }

    ngOnInit(){
        this.addPetService.pets.subscribe(
            pets => this.pets = pets,
            error => console.log(error.message)
        );
        this.addPetService.load_users_pets(this.userid);
    }
}
