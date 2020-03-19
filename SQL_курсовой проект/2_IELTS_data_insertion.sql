# DATA INJECTION FOR IELTS DB
use ielts;

INSERT INTO exams
 SET
 	id = 1,
 	`type`= 'regular',
 	format = 'paper-based',
 	module = 'Academic';
 
INSERT INTO exams
 SET
 	id = 2,
 	`type`= 'regular',
 	format = 'paper-based',
 	module = 'General';
 
INSERT INTO exams
 SET
 	id = 3,
 	`type`= 'regular',
 	format = 'computer-based',
 	module = 'Academic';
 
 INSERT INTO exams
 SET
 	id = 4,
 	`type`= 'regular',
 	format = 'computer-based',
 	module = 'General';
 
 INSERT INTO exams
 SET
 	id = 5,
 	`type`= 'ukvi',
 	format = 'paper-based',
 	module = 'Academic';
 
 INSERT INTO exams
 SET
 	id = 6,
 	`type`= 'ukvi',
 	format = 'paper-based',
 	module = 'General';
 
 INSERT INTO exams
 SET
 	id = 7,
 	`type`= 'ukvi',
 	format = 'computer-based',
 	module = 'Academic';
 
 INSERT INTO exams
 SET
 	id = 8,
 	`type`= 'ukvi',
 	format = 'life skills',
 	module = 'A1';
 
 
 INSERT INTO exams
 SET
 	id = 9,
 	`type`= 'ukvi',
 	format = 'life skills',
 	module = 'B1';
 
 INSERT INTO centres (id, name) VALUES 
 (1, 'RU045'),
 (2, 'RU069'),
 (3, 'RU110');

INSERT INTO cities (id, name, centre_id, `type`, price_regular) VALUES
(1, 'Vladivostok', 1, 'head', 16000),
(2, 'Irkutsk', 1, 'regional', 19500),
(3, 'Moscow', 2, 'head', 14000),
(4, 'Samara', 2, 'regional', 18000),
(5, 'Ekaterinburg', 2, 'regional', 19000),
(6, 'Novosibirsk', 2, 'regional', 23500),
(7, 'St.Petersburg', 3, 'head', 16000),
(8, 'Kaliningrad', 3, 'regional', 19000);

INSERT INTO locations (id, name, city_id, address, max_allocation) VALUES
(1, 'Alpha Hotel', 3, 'Izmailovskoe shosse, 71A', 500);

INSERT INTO `users` (`id`, `login`, `password_hash`, `created_at`, `updated_at`, `email`, `deposit`) VALUES ('1', '55txmf', '01703a53c0c238bb6faf4095b6eba7268d62683d', NOW(), NOW(), 'joseph.mclaughlin@example.org', NULL);
INSERT INTO `users` (`id`, `login`, `password_hash`, `created_at`, `updated_at`, `email`, `deposit`) VALUES ('2', '32jvrm', '1ec22d79e8b718a68bf9eec29a14425a5d665f1b', NOW(), NOW(), 'xprice@example.org', NULL);
INSERT INTO `users` (`id`, `login`, `password_hash`, `created_at`, `updated_at`, `email`, `deposit`) VALUES ('3', '35etqh', 'e527d47667e6c8d5ca239885343ab7adaab0d5eb', NOW(), NOW(), 'mills.dimitri@example.com', NULL);
INSERT INTO `users` (`id`, `login`, `password_hash`, `created_at`, `updated_at`, `email`, `deposit`) VALUES ('4', '98yldv', '7f39956c7408e4e60ff3769e4f2863a2b79a18b7', NOW(), NOW(), 'dillan49@example.com', NULL);
INSERT INTO `users` (`id`, `login`, `password_hash`, `created_at`, `updated_at`, `email`, `deposit`) VALUES ('5', '59rsvm', '559d57b830c2d8ea33384c392c8beab650e30c47', NOW(), NOW(), 'herman.sim@example.com', NULL);
INSERT INTO `users` (`id`, `login`, `password_hash`, `created_at`, `updated_at`, `email`, `deposit`) VALUES ('6', '94yuch', '650d663bd12d9615fb675f5c3c14a906153af64e', NOW(), NOW(), 'kreiger.mason@example.net', NULL);
INSERT INTO `users` (`id`, `login`, `password_hash`, `created_at`, `updated_at`, `email`, `deposit`) VALUES ('7', '92sgjq', '2f2ab29fded5a85e33e529d0df244bc3c80748e8', NOW(), NOW(), 'jerry72@example.net', NULL);
INSERT INTO `users` (`id`, `login`, `password_hash`, `created_at`, `updated_at`, `email`, `deposit`) VALUES ('8', '58oxju', '83c307d376df1d53532da3a7bc5b29b3c9c5bc48', NOW(), NOW(), 'bednar.matilde@example.org', NULL);
INSERT INTO `users` (`id`, `login`, `password_hash`, `created_at`, `updated_at`, `email`, `deposit`) VALUES ('9', '89drsj', '0d34aaaf33c772c2389b6be51284254a7d868b6f', NOW(), NOW(), 'jdurgan@example.com', NULL);
INSERT INTO `users` (`id`, `login`, `password_hash`, `created_at`, `updated_at`, `email`, `deposit`) VALUES ('10', '02rvia', '2330335004cdac4aa13785a999c88781c4ead63b', NOW(), NOW(), 'qlabadie@example.org', NULL);
INSERT INTO `users` (`id`, `login`, `password_hash`, `created_at`, `updated_at`, `email`, `deposit`) VALUES ('11', '13kkhg', '2c16aa261feececca5a95de81045ef0d5982570e', NOW(), NOW(), 'nya.considine@example.net', NULL);
INSERT INTO `users` (`id`, `login`, `password_hash`, `created_at`, `updated_at`, `email`, `deposit`) VALUES ('12', '75djpy', '8dfff832f373443ceca9a29cbba027d48f7237d7', NOW(), NOW(), 'smitham.simone@example.org', NULL);
INSERT INTO `users` (`id`, `login`, `password_hash`, `created_at`, `updated_at`, `email`, `deposit`) VALUES ('13', '40lewm', 'edadba1b333abbbc6a87344cbab540f70160bcaf', NOW(), NOW(), 'leonel72@example.com', NULL);
INSERT INTO `users` (`id`, `login`, `password_hash`, `created_at`, `updated_at`, `email`, `deposit`) VALUES ('14', '10attx', '1337941ee9a28272c2d7bb934b1bd3f395826c6c', NOW(), NOW(), 'ewisozk@example.com', NULL);
INSERT INTO `users` (`id`, `login`, `password_hash`, `created_at`, `updated_at`, `email`, `deposit`) VALUES ('15', '17jfxz', '6202e0eb9ec86e284c6ea5b40a530bfee0044fc1', NOW(), NOW(), 'derrick47@example.org', NULL);
INSERT INTO `users` (`id`, `login`, `password_hash`, `created_at`, `updated_at`, `email`, `deposit`) VALUES ('16', '96bfch', 'edfeb82ded153a4a222c239b76dbf5258c42d636', NOW(), NOW(), 'zrunte@example.net', NULL);
INSERT INTO `users` (`id`, `login`, `password_hash`, `created_at`, `updated_at`, `email`, `deposit`) VALUES ('17', '61mmub', '2b2f7de3cd2e7840e11b6086b79ca3eb937439cb', NOW(), NOW(), 'hand.kacie@example.org', NULL);
INSERT INTO `users` (`id`, `login`, `password_hash`, `created_at`, `updated_at`, `email`, `deposit`) VALUES ('18', '88uxdy', '74234d687c6fe6920dbb7aafdc26ced55ae22354', NOW(), NOW(), 'emmanuel31@example.net', NULL);
INSERT INTO `users` (`id`, `login`, `password_hash`, `created_at`, `updated_at`, `email`, `deposit`) VALUES ('19', '03tlpr', '4966d349550aee69544fd0a8d31f9845c56def7a', NOW(), NOW(), 'simeon.aufderhar@example.com', NULL);
INSERT INTO `users` (`id`, `login`, `password_hash`, `created_at`, `updated_at`, `email`, `deposit`) VALUES ('20', '94tfvz', '3bf83207e43dd4665e1c0350e4e6ce660ac5686a', NOW(), NOW(), 'chadd79@example.org', NULL);
INSERT INTO `users` (`id`, `login`, `password_hash`, `created_at`, `updated_at`, `email`, `deposit`) VALUES ('21', '51hkzw', '013c9d97c8d9dd4218f9bb236e5e1ff04f43f420', NOW(), NOW(), 'fbergstrom@example.net', NULL);
INSERT INTO `users` (`id`, `login`, `password_hash`, `created_at`, `updated_at`, `email`, `deposit`) VALUES ('22', '91wfrk', '3ca59a933377a3553e6180fe1fcc4589af50f506', NOW(), NOW(), 'lera66@example.net', NULL);
INSERT INTO `users` (`id`, `login`, `password_hash`, `created_at`, `updated_at`, `email`, `deposit`) VALUES ('23', '81pnoe', 'fa4d4aff98b66d6e59de868cbb889d34e70b8233', NOW(), NOW(), 'rae72@example.org', NULL);
INSERT INTO `users` (`id`, `login`, `password_hash`, `created_at`, `updated_at`, `email`, `deposit`) VALUES ('24', '79ujtn', 'e96e01f647c6ead77febcc091ca78ca8b543deee', NOW(), NOW(), 'melissa65@example.com', NULL);
INSERT INTO `users` (`id`, `login`, `password_hash`, `created_at`, `updated_at`, `email`, `deposit`) VALUES ('25', '20mxgu', '9f3342d84743c3d6be4176752fde7cab3d845f2e', NOW(), NOW(), 'allie.langworth@example.org', NULL);
INSERT INTO `users` (`id`, `login`, `password_hash`, `created_at`, `updated_at`, `email`, `deposit`) VALUES ('26', '49cqmi', 'a9ec7989d5439f512c7c1b097749c112ccbf419e', NOW(), NOW(), 'ethel.conn@example.com', NULL);
INSERT INTO `users` (`id`, `login`, `password_hash`, `created_at`, `updated_at`, `email`, `deposit`) VALUES ('27', '61ylpx', '2b95179482fcf7c1b648a3c11b9c32ab5ab36b24', NOW(), NOW(), 'name.langosh@example.net', NULL);
INSERT INTO `users` (`id`, `login`, `password_hash`, `created_at`, `updated_at`, `email`, `deposit`) VALUES ('28', '97sfzn', '86cdac1f629c26bd48e4d8d5bdbb5dce7eec65f3', NOW(), NOW(), 'owehner@example.com', NULL);
INSERT INTO `users` (`id`, `login`, `password_hash`, `created_at`, `updated_at`, `email`, `deposit`) VALUES ('29', '34xjae', '3969251aa4557b7d6d8c0f10678df74e2d6464b5', NOW(), NOW(), 'shawna.fay@example.org', NULL);
INSERT INTO `users` (`id`, `login`, `password_hash`, `created_at`, `updated_at`, `email`, `deposit`) VALUES ('30', '78bmir', 'ee71a2c0f13d334774778365d46fd4239bf7bca7', NOW(), NOW(), 'durward.emard@example.org', NULL);
INSERT INTO `users` (`id`, `login`, `password_hash`, `created_at`, `updated_at`, `email`, `deposit`) VALUES ('31', '70oyry', '5670fae34663580d74eaa38a0ab97cd64c22a7b4', NOW(), NOW(), 'lschoen@example.com', NULL);
INSERT INTO `users` (`id`, `login`, `password_hash`, `created_at`, `updated_at`, `email`, `deposit`) VALUES ('32', '94xczz', '4f1f329b62096b5df468e8cdc3439d2623a90658', NOW(), NOW(), 'wupton@example.net', NULL);
INSERT INTO `users` (`id`, `login`, `password_hash`, `created_at`, `updated_at`, `email`, `deposit`) VALUES ('33', '20gbxw', '255953daa556513ee570f44d2c087327dd8964df', NOW(), NOW(), 'jcorkery@example.net', NULL);
INSERT INTO `users` (`id`, `login`, `password_hash`, `created_at`, `updated_at`, `email`, `deposit`) VALUES ('34', '52mggw', '76b62a9bff52f30fc2d7091d693cafb7f518220f', NOW(), NOW(), 'foster85@example.com', NULL);
INSERT INTO `users` (`id`, `login`, `password_hash`, `created_at`, `updated_at`, `email`, `deposit`) VALUES ('35', '60ocxd', '4ff2406d022b6f73b2ab62dd54374271020b9c85', NOW(), NOW(), 'wilburn.mante@example.com', NULL);

INSERT INTO profiles (user_id, given_name, family_name, `d.o.b.`, phone_number, hometown, address, created_at, updated_at) VALUES 
(13, 'Mark', 'Wolovitz', '1990-07-13', '+79637896565', 'Moscow', 'Noviy Arbat, 15a, 120', NOW(), NOW()),
(14, 'Anton', 'Gorodov', '1990-07-13', '+79635468767', 'Moscow', 'Noviy Arbat, 10, 22', NOW(), NOW()),
(15, 'Sergey', 'Katz', '1990-07-13', '+79630987689', 'Moscow', 'Profsoyuznaya, 32, 111', NOW(), NOW()),
(16, 'Ivan', 'Poddolniy', '1990-07-13', '+79631426688', 'Moscow', 'Bolshaya Nikitskaya, 59, 10', NOW(), NOW()),
(17, 'Alexey', 'Shelepov', '1990-07-13', '+79097770432', 'Moscow', 'Lesnaya st., 1a, 6', NOW(), NOW()),
(18, 'Alexey', 'Revazov', '1990-07-13', '+79630002211', 'Moscow', 'Ulitsa gen. Tyuleneva, 4v, 47', NOW(), NOW()),
(19, 'Sofia', 'Ivanova', '1990-07-13', '+79680107774', 'Moscow', 'Krasnoselskaya naberezhnaya, 11, 10', NOW(), NOW()),
(20, 'Anna', 'Ivanova', '1990-07-13', '+79638968012', 'Moscow', 'Obolenova st., 2b, 70', NOW(), NOW()),
(21, 'Ulukbek', 'Sammatov', '1990-07-13', '+79121224937', 'Moscow', 'Shestoy Rabochiy per., 9, 50', NOW(), NOW()),
(22, 'Asylzhan', 'Beybut', '1990-07-13', '+79188550101', 'Moscow', 'Turgenevskaya, 13, 2', NOW(), NOW());

 INSERT INTO sessions
 SET
 	id = 1,
 	`date` = '2019-12-14',
 	exam_id = 3,
 	centre_id = 2,
 	city_id = 3,
 	location_id = 1,
 	allocated = 15,
 	taken = 0,
 	created_at = NOW(),
 	updated_at = NOW();
 
 INSERT INTO candidates
 SET 
 	id = 1,
 	user_id = 16,
 	session_id = 1,
 	exam_id = 3,
 	status = 'active',
 	payment_status = 'awaiting payment',
 	payment_id = NULL,
 	created_at = NOW(),
 	updated_at = NOW();
 	
 INSERT INTO candidates
 SET 
 	id = 2,
 	user_id = 18,
 	session_id = 1,
 	exam_id = 3,
 	status = 'active',
 	payment_status = 'awaiting payment',
 	payment_id = NULL,
 	created_at = NOW(),
 	updated_at = NOW();
 	

 
 
  