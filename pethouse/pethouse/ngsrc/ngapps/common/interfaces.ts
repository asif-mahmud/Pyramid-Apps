/**
 * Created by shimon on 11/9/16.
 */
export interface Pet{
    name:string,
    type:number,
    description:string
}

export interface PetObj{
    name:string,
    type:string,
    owner:string,
    description:string
}

export interface PetType{
    id:number,
    name:string
}


export interface VStatus{
    success:boolean,
    msg_stack:string[]
}
