package com.masai.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.masai.service.RequestService;

@RestController
@CrossOrigin(origins = "*")
public class RequestController {

	@Autowired
	private RequestService requestService;
	
	@GetMapping("/getResponse")
	public String chat(@RequestParam("prompt") String prompt) {
	
		return requestService.getMyGptResponse(prompt);
		
	}
	
	
}
