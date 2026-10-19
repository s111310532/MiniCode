while iteration < self.max_iterations:
            iteration += 1

            response = await self.provider.chat(
                messages=self._microcompact(messages),
                tools=self.tools.get_definitions(),
                model=self.model,
                reasoning_effort=self.reasoning_effort,
            )

            if response.has_tool_calls:
                # Record the assistant turn that requested tools.
                tool_call_dicts = [
                    {
                        "id": tc.id,
                        "type": "function",
                        "function": {
                            "name": tc.name,
                            # Must be JSON string
                            "arguments": json.dumps(tc.arguments),
                        },
                    }
                    for tc in response.tool_calls
                ]
                messages = self.context.add_assistant_message(
                    messages,
                    response.content,
                    tool_call_dicts,
                    reasoning_content=response.reasoning_content,
                    thinking_blocks=response.thinking_blocks,
                )
                session.add_message(
                    "assistant",
                    messages[-1]["content"],
                    tool_calls=tool_call_dicts,
                )
