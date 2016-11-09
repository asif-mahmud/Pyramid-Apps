/**
 * Created by shimon on 11/8/16.
 */
import {Component, OnInit} from "@angular/core";
import "rxjs/add/operator/map";
import "rxjs/add/operator/catch";
import {AddPetService} from "common/addpet.service";
import {PetTypeService} from "common/pettypes.service";
import {Pet, PetType, VStatus} from "common/interfaces";


@Component({
    selector:"add-pet-form",
    templateUrl:"/ngapps/addpet/addpet.form.html",
})
export class AddPetFormComponent implements OnInit{
    petTypes: PetType[];
    pet:Pet;
    vstatus:VStatus;
    submitted:boolean;

    constructor(
        private petTypesService:PetTypeService,
        private addPetService:AddPetService
    ){
        this.pet = {name:"", type:0, description:''};
        this.vstatus = {success:false, msg_stack:[]};
        this.submitted = false;
        console.log(this.addPetService);
    }

    ngOnInit(){
        this.petTypesService.pet_types.subscribe(
            types => this.petTypes = types,
            error => console.log(error.message)
        );
        this.addPetService.status.subscribe(
            status => this.onStatusFound(status),
            error => console.log(error.message)
        );
        this.petTypesService.load_all();
    }

    onSubmit(){
        this.addPetService.add_pet(this.pet);
    }

    onStatusFound(status){
        this.vstatus = status;
        this.submitted = true;
    }
}
