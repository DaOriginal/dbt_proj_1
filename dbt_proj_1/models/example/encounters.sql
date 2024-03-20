
{{ config(materialized='table') }}

with get_encounters as (

 select 
patient_id as person_id,
encounter_id ,
encounter_type ,
encounter_datetime as visit_date ,
program_id ,
location_id,
creator ,
date_created ,
date_changed ,
voided ,
voided_by ,
void_reason ,
date_voided,
"uuid",
provider_id
from 
encounter
)

select *
from get_encounters
