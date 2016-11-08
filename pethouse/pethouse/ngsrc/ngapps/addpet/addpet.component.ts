/**
 * Created by shimon on 11/8/16.
 */
import {Component, AfterViewInit} from "@angular/core";
import {Http, Headers, RequestOptions} from "@angular/http";

declare var jQuery:any;

@Component({
    selector:"add-pet-form",
    templateUrl:"/ngapps/addpet/addpet.form.html"
})
export class AddPetFormComponent implements AfterViewInit{
    constructor(private http:Http){
    }

    ngAfterViewInit(){
        jQuery(".ui.dropdown").dropdown();
    }
}
