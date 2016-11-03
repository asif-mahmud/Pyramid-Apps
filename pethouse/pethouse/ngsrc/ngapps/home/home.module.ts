/**
 * Created by shimon on 11/3/16.
 */

import {NgModule} from "@angular/core";
import {BrowserModule} from "@angular/platform-browser";
import {HomePageComponent} from "./home.component";


@NgModule({
    imports:[BrowserModule],
    declarations:[HomePageComponent],
    bootstrap:[HomePageComponent]
})
export class HomePageModule{}
