alter table Booking_Master add constraint fk_enquiry
foreign key(Enquiry_Id) references Enquiry_Master(Enquiry_Id);