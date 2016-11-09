/**
 * Created by shimon on 11/8/16.
 */
import {BrowserModule} from "@angular/platform-browser";
import {NgModule} from "@angular/core";
import {HttpModule, JsonpModule} from "@angular/http";
import {PetCollectionComponent} from "./component";
import {AddPetService} from "common/addpet.service";


@NgModule({
    imports:[BrowserModule, HttpModule, JsonpModule],
    declarations:[PetCollectionComponent],
    bootstrap:[PetCollectionComponent],
    providers:[AddPetService]
})
export class PetCollectionApp{}
