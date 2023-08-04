package com.masai.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class ServiceImpl implements RequestService{

	@Autowired
	private RestTemplate restTemplate;
	
	String key = "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";
	String model = "gpt-3.5-turbo";
	String url = "https://api.openai.com/v1/chat/completions";
	
	
	@Override
	public String getMyGptResponse(String userInput) {
		// TODO Auto-generated method stub
		
		HttpHeaders headers = new HttpHeaders();
		headers.setContentType(MediaType.APPLICATION_JSON);
		headers.set("Authorization", "Bearer" +"key");
		
		String requestBody = "{\"model\":\"" + model +  
				"\",\"messages\" : [{\"role\" : \"user\",\"content\" :\""
				+ userInput + "\"}]]";
		
		HttpEntity<String> request = new HttpEntity<>(requestBody,headers);
		return restTemplate.postForObject(url, request, String.class);
	}

}
