
insert into asterisk.ps_aors (id, max_contacts) values ('101', 1);
insert into asterisk.ps_aors (id, max_contacts) values ('102', 1);

insert
into asterisk.ps_auths
(id, auth_type, password, username)
values
('101', 'userpass', '123456', '101');

insert
into asterisk.ps_auths
(id, auth_type, password, username)
values
('102', 'userpass', '123456', '102');

insert
into asterisk.ps_endpoints
(id, transport, aors, auth, context, disallow, allow, direct_media)
values
('101', 'transport-udp', '101', '101', 'internal', 'all', 'alaw', 'no'),
('102', 'transport-udp', '102', '102', 'internal', 'all', 'alaw', 'no');

